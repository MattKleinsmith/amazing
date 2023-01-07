result = `
    product = Product(
        seller=seller,
        title="${document.querySelector("#productTitle").textContent.trim()}",
        price="${document.querySelector(".a-price.a-text-price>span").textContent.replace('$', '')}",
        description="${Array.from(document.querySelectorAll("#feature-bullets>ul>li>span")).map(ele => ele.textContent.trim()).join("\n")}"
    )

    db.session.add_all([
`

product_image_urls = Array.from(document.querySelectorAll(".a-button-text>img")).map(img => img.src).filter(url => url.includes("SS40_.")).map(url => url.replace("SS40", "SL1500"));
product_image_urls.forEach((url, i) => {
    result += `
        ProductImage(
            product=product,
            url=upload_image_to_bucket_from_url("${url}"),
            preview=${i === 0 ? "True" : "False"},
            position=${i + 1}
        ),
    `
})

ratings = Array.from(document.querySelectorAll(".a-icon.a-icon-star.review-rating>span")).map(ele => ele.innerText.split(" ")[0]).slice(0, 5);
reviews = Array.from(document.querySelectorAll(".reviewText>span")).map(ele => ele.innerHTML.replaceAll("<br>", "&#13;").replaceAll('"', "'")).slice(0, 5);
titles = Array.from(document.querySelectorAll(".review-title-content>span")).map(ele => ele.innerText).slice(0, 5);
users = ["brian", "caitlynn", "derrik", "elizabeth", "sarah"];

ratings.forEach((rating, i) => {
    result += `
        Review(
            buyer=${users[i]},
            product=product,
            rating=${rating},
            review="${reviews[i]}",
            title="${titles[i]}"
        ),
    `
});

result += '])'

result += '\n\n    db.session.commit()'

console.log(result)
