function checkAnagrams(first, second) {
  const firstTrimmed = first.toLowerCase().replace("\s", "");
  const secondTrimmed = second.toLowerCase().replace("\s", "");
  if (firstTrimmed.length !== secondTrimmed.length) return false;

  const firstSorted = Array.from(firstTrimmed).sort();
  const secondSorted = Array.from(secondTrimmed).sort();
  return firstSorted.every((c, i) => c == secondSorted[i]);
}
