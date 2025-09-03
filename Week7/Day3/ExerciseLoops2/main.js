let names = ["john", "sarah", 23, "Rudolf", 34];

console.log("#1");
for (let name of names) {
  if (typeof name !== "string") {
    continue;
  }
  if (name[0] !== name[0].toLocaleUpperCase()) {
    console.log(name[0].toLocaleUpperCase() + name.slice(1));
  }
}

console.log("#2");
for (let name of names) {
  if (typeof name !== "string") break;

  console.log(name);
}
