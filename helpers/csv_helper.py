import csv


def result_to_csv(results_in_dict):
    with open('./files/pesq_results.csv', 'w', encoding='UTF8') as f:
        header = ['fileName', 'PESQ_narrow_band', 'PESQ_wide_band']
        writer = csv.writer(f)
        writer.writerow(header)

        for i in results_in_dict.keys():
            data = [i, results_in_dict[i]["narrow_band"], results_in_dict[i]["wide_band"]]
            writer.writerow(data)
