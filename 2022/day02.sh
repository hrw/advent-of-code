#!/bin/sh

input="day02.data"

wynik1=0
wynik2=0

while IFS= read -r line
do
  case $line in
    "A X")
      wynik1=$(( ${wynik1} + 4))
      wynik2=$(( ${wynik2} + 3))
      ;;
    "A Y")
      wynik1=$(( ${wynik1} + 8))
      wynik2=$(( ${wynik2} + 4))
    ;;
    "A Z")
      wynik1=$(( ${wynik1} + 3))
      wynik2=$(( ${wynik2} + 8))
    ;;
    "B X")
      wynik1=$(( ${wynik1} + 1))
      wynik2=$(( ${wynik2} + 1))
    ;;
    "B Y")
      wynik1=$(( ${wynik1} + 5))
      wynik2=$(( ${wynik2} + 5))
    ;;
    "B Z")
      wynik1=$(( ${wynik1} + 9))
      wynik2=$(( ${wynik2} + 9))
    ;;
    "C X")
      wynik1=$(( ${wynik1} + 7))
      wynik2=$(( ${wynik2} + 2))
    ;;
    "C Y")
      wynik1=$(( ${wynik1} + 2))
      wynik2=$(( ${wynik2} + 6))
    ;;
    "C Z")
      wynik1=$(( ${wynik1} + 6))
      wynik2=$(( ${wynik2} + 7))
    ;;
  esac

done < "$input"

echo $wynik1
echo $wynik2
