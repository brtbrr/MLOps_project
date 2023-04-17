from argparse import ArgumentParser

import arxiv

from .process_paper import process_result

parser = ArgumentParser()
parser.add_argument("--query", type=str)
parser.add_argument("--max_results", type=int, default=1)


# toDo fix dates
def main(query, max_results):
    search = arxiv.Search(
        query=query, max_results=max_results, sort_by=arxiv.SortCriterion.SubmittedDate
    )
    num_processed = 0
    for result in search.results():
        # toDo logging
        print(f"processing paper {num_processed }")
        process_result(result)
        num_processed += 1


if __name__ == "__main__":
    args = parser.parse_args()
    query = args.query
    max_results = args.max_results
    main(query, max_results)
