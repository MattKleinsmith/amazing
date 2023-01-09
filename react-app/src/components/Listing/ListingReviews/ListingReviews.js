import styles from "./ListingReviews.module.css";

import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";

import { getReviewsByProductId } from "../../../store/reviews";

import ListingReviewsBreakdown from "./ListingReviewsBreakdown/ListingReviewsBreakdown";
import ListingReviewsList from "./ListingReviewsList/ListingReviewsList";

export default function ListingReviews({ product, setReviewPosition }) {
    const dispatch = useDispatch();
    const ref = useRef();

    useEffect(() => {
        if (ref.current) setReviewPosition(ref.current.offsetTop);
    }, [ref, setReviewPosition]);

    useEffect(() => {
        dispatch(getReviewsByProductId(product.id));
    }, [dispatch, product]);

    const reviews = useSelector(state => Object.values(state.reviews));

    return (
        <div ref={ref} className={styles.wrapper}>
            <ListingReviewsBreakdown product={product} reviews={reviews} />
            <ListingReviewsList product={product} reviews={reviews} />
        </div>
    );
}
