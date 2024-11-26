function showRetailers() {
  const retailers = [
    { name: "T&T Supermarket", location: "Toronto, ON" },
    { name: "H-Mart", location: "Vancouver, BC" },
    { name: "J-Town", location: "Markham, ON" },
    { name: "Foody World", location: "Calgary, AB" },
  ];

  const retailerList = document.getElementById("retailer-list");

  retailerList.innerHTML = "";

  const ul = document.createElement("ul");

  retailers.forEach((retailer) => {
    const li = document.createElement("li");
    li.textContent = `${retailer.name} - ${retailer.location}`;
    ul.appendChild(li);
  });

  retailerList.appendChild(ul);

  retailerList.style.display = "block";
}
