import pandas as pd


def advancedStats(data, labels):
    '''Advanced stats should leverage pandas to calculate
    some relevant statistics on the data.

    data: numpy array of data
    labels: numpy array of labels
    '''
    
    # convert to dataframe
    df = pd.DataFrame(data)

    # print skew and kurtosis for every column
    skew = df.skew()
    kurtosis = df.kurtosis()
    for i in range(0, len(skew)):
        print("\nColumn {} statistics:\n".format(i))
        print("Skew: {} Kurtosis:{}".format(skew[i],kurtosis[i]))
    
    # assign in labels
    df["labels"] = labels

    print("\n\nDataframe statistics")

    # groupby labels into "benign" and "malignant"
    df.groupby(labels)

    # collect means and standard deviations for columns, grouped by label
    mean = df.groupby(["labels"]).mean()
    standard_deviation = df.groupby(["labels"]).std()

    # Print mean and standard deviation for Benign
    print("Benign Stats:")
    print("Mean:\n")
    print(mean.loc["B", :])
    print("Standard Deviation:\n")
    print(standard_deviation.loc["B", :])
    print("\n")

    # Print mean and standard deviation for Malignant
    print("Malignant Stats:")
    print("Mean:\n")
    print(mean.loc["M", :])
    print("Standard Deviation:\n")
    print(standard_deviation.loc["M", :])
    print("\n")
