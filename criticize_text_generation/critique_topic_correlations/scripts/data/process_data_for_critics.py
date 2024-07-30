import os
import json
import argparse
import random
import collections


parser = argparse.ArgumentParser(description='Process raw json files to generate training data for fitting critic generative processes.')
parser.add_argument('--vocab_file', type=str, required=True,
                    help='Vocabulary file generated by scripts/data/build_data_for_critics.py. Should be data_folder/train.json.CTM.vocab.')
parser.add_argument('--data_file', type=str, required=True,
                    help='Text in json format. Can be either ground truth data or LM generations.')
parser.add_argument('--shuffle', action='store_true',
                    help='Shuffle or not.')
parser.add_argument('--seed', type=int, default=1234,
                    help='Random seed.')
args = parser.parse_args()


def load_vocab(vocab_filename):
    stoi = {}
    with open(vocab_filename) as fin:
        for line in fin:
            stoi[line.strip()] = len(stoi)
    return stoi


def process_data(filename, filename_out, stoi, shuffle=False):
    data = json.load(open(filename))
    outputs = []
    with open(filename_out, 'w') as fout:
        for example in data:
            sections = example['sections']
            words = ' '.join(sections)
            words = words.replace('\n', ' ')
            words = words.split()
            word_ids = [stoi[word] for word in words if word in stoi]
            counts = collections.Counter(word_ids)
            s = ' '.join([f'{key}:{counts[key]}' for key in counts])
            total = len(counts)
            if total == 0:
                continue
            s = f'{total} {s}\n'
            outputs.append(s)
        if shuffle:
            random.shuffle(outputs)
        for output in outputs:
            fout.write(output)


def main(args):
    vocab_filename = args.vocab_file
    stoi = load_vocab(vocab_filename)

    random.seed(args.seed)
    filename = args.data_file
    filename_out = filename + '.CTM.id'
    process_data(filename, filename_out, stoi, args.shuffle)


if __name__ == '__main__':
    main(args)
