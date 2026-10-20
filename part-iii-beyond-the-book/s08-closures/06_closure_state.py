"""Mutating the Closure State"""

def mean() -> callable:
    """Creates a mutable mean function that updates as numbers are added"""
    sample = []
    def inner_mean(n: int) -> float:
        sample.append(n)
        return sum(sample) / len(sample)
    return inner_mean

def main() -> None:
    """Main function"""
    sample_mean = mean()
    for i in range(1, 6):
        print(f"Stored {i}: Mean = {sample_mean(i)}")

if __name__ == "__main__":
    main()
