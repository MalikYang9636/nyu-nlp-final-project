#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from typing import Tuple, Dict


def parse_input(input_file: str) -> Dict[int, Tuple[str, str]]:
    with open(input_file, "r") as f:
        lines = f.readlines()
    label_dict: Dict[int, Tuple[str, str]] = {}
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split("\t")
        if len(parts) == 1 or len(parts) == 5:
            continue
        elif len(parts) == 2 or len(parts) >= 6:
            label_dict[i] = (parts[0], parts[1] if len(
                parts) == 2 else parts[5])
        else:
            print(f"Error: line {i + 1} is not in the correct format.")
            exit(1)
    return label_dict


def score(key_label_dict: Dict[int, Tuple[str, str]],
          response_label_dict: Dict[int, Tuple[str, str]]) -> Tuple[float, float, float]:
    """
    Computes the precision, recall and f1-score of the response file.
    """
    correct = 0
    key_total = 0
    response_total = 0
    key_ids = []
    response_ids = []
    for i in key_label_dict.keys():
        if key_label_dict[i][1].startswith("ARG"):
            key_total += 1
            key_ids.append(i)
        if i not in response_label_dict.keys():
            continue
        if key_label_dict[i][0] != response_label_dict[i][0]:
            print(
                f"Error: key and response file does not match on line {i + 1}.")
            exit(1)
        if response_label_dict[i][1].startswith("ARG"):
            response_total += 1
            response_ids.append(i)
        if not key_label_dict[i][1].startswith("ARG") and not response_label_dict[i][1].startswith("ARG"):
            continue
        if key_label_dict[i][1] == response_label_dict[i][1]:
            correct += 1
    for i in response_label_dict.keys():
        if i not in key_label_dict.keys():
            if response_label_dict[i][1].startswith("ARG"):
                response_total += 1
                response_ids.append(i)
    key_ids.sort()
    response_ids.sort()
    print(f"Keys: {key_ids}")
    print(f"Responses: {response_ids}")
    print(f"Correct: {correct}")
    print(f"Key total: {key_total}")
    print(f"Response total: {response_total}")
    precision = correct / response_total
    recall = correct / key_total
    f1 = 2 * precision * recall / (precision + recall)
    return precision, recall, f1


def main():
    parser = argparse.ArgumentParser(
        description="A scoring script for Maxent semantic role labeling")
    parser.add_argument("keyfile", help="input key file")
    parser.add_argument("responsefile", help="input response file")
    args = parser.parse_args()

    print("Parsing key file...")
    key_label_dict = parse_input(args.keyfile)
    print("Parsing response file...")
    response_label_dict = parse_input(args.responsefile)

    precision, recall, f1 = score(key_label_dict, response_label_dict)
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-score: {f1}")


if __name__ == '__main__':
    main()
