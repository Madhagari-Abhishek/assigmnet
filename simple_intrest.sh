#!/bin/bash

# Function to calculate simple interest
calculate_simple_interest() {
    principal=$1
    rate=$2
    time=$3

    interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)
    echo "Simple interest: $interest"
}

# Main script
echo "Enter principal amount: "
read principal

echo "Enter annual interest rate (in percentage): "
read rate

echo "Enter time duration (in years): "
read time

calculate_simple_interest $principal $rate $time
