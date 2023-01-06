import styles from "./ListingReviews.module.css";

import { useDispatch, useSelector } from "react-redux";

import { getReviewsByProductId } from "../../../store/reviews";

import ListingReviewsBreakdown from "./ListingReviewsBreakdown/ListingReviewsBreakdown";
import ListingReviewsList from "./ListingReviewsList/ListingReviewsList";
import { useEffect } from "react";

export default function ListingReviews({ product }) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getReviewsByProductId(product.id));
    }, [dispatch, product.id]);

    const reviews = useSelector(state => Object.values(state.reviews));

    return (
        <div className={styles.wrapper}>
            <ListingReviewsBreakdown product={product} reviews={reviews} />
            <ListingReviewsList product={product} reviews={reviews} />
        </div>
    );
}
