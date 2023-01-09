import styles from "./Listing.module.css";

import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useSearchParams } from "react-router-dom";

import { getProductDetails } from "../../store/productDetails";

import ListingLeft from "./ListingLeft/ListingLeft";
import ListingMiddle from "./ListingMiddle/ListingMiddle";
import ListingRight from "./ListingRight/ListingRight";
import ListingReviews from "./ListingReviews/ListingReviews";

export default function Listing() {
    const dispatch = useDispatch();
    const { productId } = useParams();

    const [reviewPosition, setReviewPosition] = useState(0);

    const productDetails = useSelector(state => state.productDetails);
    const product = productDetails[productId];

    const source = useSearchParams()[0].get("source");
    if (source) window.scrollTo(0, 10000);

    useEffect(() => {
        dispatch(getProductDetails(productId));
        window.scrollTo(0, 0);
    }, [productId, dispatch]);

    if (!product) return;

    document.title = `Amazing: ${product.title}`;

    return (
        <div className={styles.wrapper}>
            <div className={styles.top}>
                <ListingLeft product={product} />
                <ListingMiddle product={product} reviewPosition={reviewPosition} />
                <ListingRight product={product} />
            </div>
            <div className={styles.reviews}>
                <ListingReviews product={product} setReviewPosition={setReviewPosition} />
            </div>
        </div>
    );
}
