import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Dynamic Pricing deployment pipeline.")
    parser.add_argument("--input_table", type=str, default=None)
    parser.add_argument("--output_table", type=str, default=None)

    args = parser.parse_args()
    input_table = args.input_table
    output_table = args.output_table

    print(f"Input table: {input_table}")
    print(f"Output table: {output_table}")
