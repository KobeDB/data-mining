#include <stdio.h>
#include "rapidcsv.h"

int main() {
    printf("Hello there\n");

    rapidcsv::Document doc{"data/retail.csv"};

    std::vector<float> col = doc.GetColumn<float>("Price");

    printf("Read %d values\n", col.size());
}