import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import styles from "./Listing.module.css";
import ListingLeft from "./ListingLeft/ListingLeft";
import ListingRight from "./ListingRight/ListingRight";
import { getProduct } from "../../store/productDetails";

export default function Listing() {
    const { productId } = useParams();
    const productDetails = useSelector(state => state.productDetails);
    const product = productDetails[productId];

    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProduct);
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
