"""
A utility script for transcribing an entire folder of audio files. This script was used to transcribe the files from
the librispeech and CV test datasets; the results were then separately fed through a word error rate script.
"""

import argparse
import os
from time import time

import torch
from torch.utils.data import DataLoader
from tqdm import tqdm

from ocotillo.dataset import AudioFolderDataset
from ocotillo.model_loader import load_model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Input folder containing audio files you want transcribed.')
    parser.add_argument('--output_file', default='transcribed.txt', help='Where transcriptions will be placed.')
    parser.add_argument('--phonetic', default=False, help='Whether or not to output phonetic symbols.')
    parser.add_argument('--resume', default=0, type=int, help='Skip the first <n> audio tracks.')
    parser.add_argument('--batch_size', default=8, type=int, help='Number of audio files to process at a time. Larger batches are more efficient on a GPU.')
    parser.add_argument('--cuda', default=-1, type=int, help='The cuda device to perform inference on. -1 (or default) means use the CPU.')
    parser.add_argument('--output_tokens', default=False, type=bool, help='Whether or not to output the CTC codes. Useful for text alignment.')
    args = parser.parse_args()

    use_torchscript = True
    if args.phonetic:
        use_torchscript = False

    model, processor = load_model(f'cuda:{args.cuda}' if args.cuda != -1 else 'cpu', use_torchscript=use_torchscript, phonetic=args.phonetic)
    # pad_limit = 566400
    pad_limit = 16000*20
    dataset = AudioFolderDataset(args.path, sampling_rate=16000, pad_to=pad_limit, skip=args.resume)
    dataloader = DataLoader(dataset, args.batch_size, num_workers=2)

    if not '/' in args.output_file:
        args.output_file = os.path.join(args.path, args.output_file)

    if args.cuda >= 0:
        model = model.cuda(args.cuda)

    start = None
    total_duration = 0
    mode = 'w' if args.resume == 0 else 'a'
    output = open(args.output_file, mode, encoding='utf-8')
    with torch.no_grad():
        for e, batch in enumerate(tqdm(dataloader)):
            if start is None:
                start = time()  # Do this here because the first batch often takes a **long** time to load and we are not measuring dataloader performance.
            max_sample_size = batch['samples'].max()
            clip = batch['clip'][:, :max_sample_size]
            total_duration += clip.shape[0] * clip.shape[-1] / 16000
            clip = [b.numpy() for b in clip]  # Because the processor takes in numpy values.
            clip = processor(clip, return_tensors='pt', padding='longest', sampling_rate=16000).input_values
            if args.cuda >= 0:
                clip = clip.cuda(args.cuda)

            logits = model(clip)[0]
            tokens = torch.argmax(logits, dim=-1)
            for b in range(tokens.shape[0]):
                # Chop off all the padding for each batch element.
                usage_percent = batch['samples'][b] / max_sample_size
                sub_tokens = tokens[b, :int(usage_percent*tokens.shape[-1])]
                # Decode and write to the output file.
                text = processor.decode(sub_tokens)
                relpath = os.path.relpath(batch['path'][b], args.path).replace('\\', '/')
                if args.output_tokens:
                    output.write(f'{text.lower()}\t{relpath}\t{sub_tokens.tolist()}\n')
                else:
                    # output.write(f'{text.lower()}\t{relpath}\n')
                    output.write(f'{relpath}|{text}\n')
            output.flush()
    stop = time()
    elapsed = stop - start
    print(f'Total elapsed: {elapsed}, processing time per second of audio input: {elapsed / total_duration} RTPR: {total_duration / elapsed}')

