import styles from "./Listing.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { getProductDetails } from "../../store/productDetails";

import ListingLeft from "./ListingLeft/ListingLeft";
import ListingMiddle from "./ListingMiddle/ListingMiddle";
import ListingRight from "./ListingRight/ListingRight";
import ListingReviews from "./ListingReviews/ListingReviews";

export default function Listing() {
    const { productId } = useParams();
    const productDetails = useSelector(state => state.productDetails);
    const product = productDetails[productId];

    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProductDetails(productId));
        window.scrollTo(0, 0);
    }, [productId, dispatch]);

    if (!product) return;

    return (

        <div className={styles.wrapper}>
            <div className={styles.top}>
                <ListingLeft product={product} />
                <ListingMiddle product={product} />
                <ListingRight product={product} />
            </div>
            <div className={styles.top}>
                <ListingReviews product={product} />
            </div>
        </div>
    );
}
