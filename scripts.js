function showRetailers() {
  const retailers = [
    { name: "T&T Supermarket", location: "Waterloo, ON" },
    { name: "Central Fresh Market", location: "Kitchener, ON" },
    { name: "Food Basics", location: "Waterloo, ON" },
    { name: "Freshco", location: "Waterloo, ON" },
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
