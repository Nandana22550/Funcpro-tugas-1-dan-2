List<int> sequenceGenerator(int start, int stop) => List.generate(stop - start + 1, (i) => start + i);

List<int> filterList(List<int> lst, bool Function(int) predicate) {
  return lst.where(predicate).toList();
}

void main() {
  final result = sequenceGenerator(1, 10);
  print(result);

  final filteredList = filterList(result, (num) => num % 2 == 0);
  print(filteredList);
}
