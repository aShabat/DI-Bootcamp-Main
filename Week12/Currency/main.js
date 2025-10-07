const API_KEY = "9219a45f07475dc86adb0559";
const form = document.getElementById("converter");
const resultP = document.getElementById("result");

(async () => {
  const response = await fetch(
    `https://v6.exchangerate-api.com/v6/${API_KEY}/codes`,
  );
  if (!response.ok)
    throw `Fetching codes gave status code '${response.status}'`;
  const result = await response.json();
  const codes = result.supported_codes;
  codes.forEach((c) => {
    const option = document.createElement("option");
    option.setAttribute("data-code", c[0]);
    option.innerHTML = `${c[0]} - ${c[1]}`;
    form.from.add(option);
    form.to.add(option.cloneNode(true));
  });
})();

form.swap.addEventListener("click", (e) => {
  e.preventDefault();
  const from = form.from.selectedIndex;
  const to = form.to.selectedIndex;
  form.from.selectedIndex = to;
  form.to.selectedIndex = from;
});

form.convert.addEventListener("click", async (e) => {
  e.preventDefault();
  const from = form.from.options[form.from.selectedIndex].dataset.code;
  const to = form.to.options[form.to.selectedIndex].dataset.code;
  const amount = form.amount.value;

  const response = await fetch(
    `https://v6.exchangerate-api.com/v6/${API_KEY}/pair/${from}/${to}/${amount}`,
  );
  if (!response.ok)
    throw `Fetching conversion gave status code '${response.status}'`;
  const result = await response.json();
  if (result.result === "success") resultP.innerHTML = result.conversion_result;
});
