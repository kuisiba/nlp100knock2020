import csv
import random


def main():

    csv.field_size_limit(1_000_000_000)
    with open("./newsCorpora.csv") as f:
        reader = csv.reader(f, delimiter='\t')
        newsCorpora = [row for row in reader]

    # Reuters, Huffington Post, Businessweek, Contactmusic.com,
    # Daily Mailだけを抽出する
    rfbcd = [row for row in newsCorpora
             if (row[3] == 'Reuters') or
             (row[3] == 'Huffington Post') or
             (row[3] == 'Businessweek') or
             (row[3] == 'Contactmusic.com') or
             (row[3] == 'Daily Mail')]

    # CATEGORYとTITLEのみ抜き出し
    pre = [[row[4], row[1]] for row in rfbcd]
    sampled = random.sample(pre, len(pre))

    train_end = int(len(sampled) * 0.8)
    valid_end = int(len(sampled) * 0.9)
    train = sampled[0:train_end]
    valid = sampled[train_end: valid_end]
    test = sampled[valid_end:]

    with open('./train.txt', 'w') as fw_train:
        writer = csv.writer(fw_train, delimiter='\t', lineterminator='\n')
        writer.writerows(train)

    with open('./valid.txt', 'w') as fw_valid:
        writer = csv.writer(fw_valid, delimiter='\t', lineterminator='\n')
        writer.writerows(valid)

    with open('./test.txt', 'w') as fw_test:
        writer = csv.writer(fw_test, delimiter='\t', lineterminator='\n')
        writer.writerows(test)


if __name__ == "__main__":
    main()
