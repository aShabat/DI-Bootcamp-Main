function checkAnagrams(first, second) {
  const firstTrimmed = first.toLowerCase().replace(" ", "");
  const secondTrimmed = second.toLowerCase().replace(" ", "");
  if (firstTrimmed.length !== secondTrimmed.length) return false;

  const firstSorted = Array.from(firstTrimmed).sort();
  const secondSorted = Array.from(secondTrimmed).sort();
  return firstSorted.every((c, i) => c == secondSorted[i]);
}
