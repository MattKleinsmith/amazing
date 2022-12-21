import { useEffect } from "react";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import styles from "./Listing.module.css";
import ListingLeft from "./ListingLeft/ListingLeft";
import ListingRight from "./ListingRight/ListingRight";

export default function Listing() {
    const { productId } = useParams();

    const products = useSelector(state => state.products);
    const product = products[productId];
    console.log("Listing - productId", productId);
    console.log("Listing - products", products);
    useEffect(() => {
        window.scrollTo(0, 0);
    })

    if (!product) return;
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <ListingLeft product={product} />
                <ListingRight product={product} />
            </div>
        </div>
    );
}
