from apyori import apriori
import pandas as pd
import os

def test_func():
    print("I have nuclear dumbass disease")



    the_data = pd.read_csv("data/test.csv")

    transactions = []
    for i in range(len(the_data)):
        transaction = the_data.columns[the_data.iloc[i] == 'Yes'].to_list()
        transactions.append(transaction)

    # transactions = [
    #     ['milk', 'bread', 'nuts', 'apple'],
    #     ['milk', 'bread', 'nuts'],
    #     ['milk', 'bread'],
    #     ['milk', 'apple'],
    #     ['bread', 'apple']
    # ]
    rules = apriori(transactions, min_support=0.1, min_confidence=0.1, min_lift=1.2)

    results = list(rules)

    for rule in results:
        items = [x for x in rule.items]
        print(f"Rule: {items}")
        print(f"Support: {rule.support}")
        for ordered_stat in rule.ordered_statistics:
            print(f"Confidence: {ordered_stat.confidence}")
            print(f"Lift: {ordered_stat.lift}")
        print("="*40)

    print("Ass rules")

    # Print association rules properly
    for rule in results:
        for ordered_stat in rule.ordered_statistics:
            antecedent = list(ordered_stat.items_base)  # LHS (condition)
            consequent = list(ordered_stat.items_add)  # RHS (result)
            
            if antecedent and consequent:  # Ensures we have a rule (not just an itemset)
                print(f"Rule: {antecedent} → {consequent}")
                print(f"Support: {rule.support:.2f}")
                print(f"Confidence: {ordered_stat.confidence:.2f}")
                print(f"Lift: {ordered_stat.lift:.2f}")
                print("=" * 40)

if __name__ == "__main__":
    print("Ok")
    df = pd.read_csv("data/retail.csv")
    
    # filter out old transactions
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    cutoff_date = pd.to_datetime('2011-01-09 12:00:00')
    df = df[df['InvoiceDate'] > cutoff_date]

    df = df[df['Description'].notna() & (df['Description'] != '')]

    print(f"{len(df)=}")

    output_folder = "output_data"
    filtered_name = "filtered_retail.csv"
    filtered_path = os.path.join(output_folder, filtered_name)

    os.makedirs(output_folder, exist_ok=True)
    df.to_csv(filtered_path, index=False)

    transactions = df.groupby('Invoice')['Description'].apply(list).reset_index()
    print(transactions.head())

    transactions_list = transactions['Description'].tolist()
    print(transactions_list[:2])

    rules = apriori(transactions_list, min_support=0.01, min_confidence=0.6, min_lift=1.2)

    results = list(rules)

    for rule in results:
        items = [x for x in rule.items]
        print(f"Rule: {items}")
        print(f"Support: {rule.support}")
        for ordered_stat in rule.ordered_statistics:
            print(f"Confidence: {ordered_stat.confidence}")
            print(f"Lift: {ordered_stat.lift}")
        print("="*40)

    print("Ass rules")

    # Print association rules properly
    for rule in results:
        for ordered_stat in rule.ordered_statistics:
            antecedent = list(ordered_stat.items_base)  # LHS (condition)
            consequent = list(ordered_stat.items_add)  # RHS (result)
            
            if antecedent and consequent:  # Ensures we have a rule (not just an itemset)
                print(f"Rule: {antecedent} → {consequent}")
                print(f"Support: {rule.support:.2f}")
                print(f"Confidence: {ordered_stat.confidence:.2f}")
                print(f"Lift: {ordered_stat.lift:.2f}")
                print("=" * 40)