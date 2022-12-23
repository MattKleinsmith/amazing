import styles from "./Listing.module.css";

import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { getProduct } from "../../store/productDetails";

import ListingLeft from "./ListingLeft/ListingLeft";
import ListingMiddle from "./ListingMiddle/ListingMiddle";
import ListingRight from "./ListingRight/ListingRight";

export default function Listing() {
    const { productId } = useParams();
    const productDetails = useSelector(state => state.productDetails);
    const product = productDetails[productId];

    const dispatch = useDispatch();
    useEffect(() => {
        dispatch(getProduct(productId));
        window.scrollTo(0, 0);
    }, [productId, dispatch]);

    if (!product) return;

    return (
        <div className={styles.wrapper}>
            <ListingLeft product={product} />
            <ListingMiddle product={product} />
            <ListingRight product={product} />
        </div>
    );
}
