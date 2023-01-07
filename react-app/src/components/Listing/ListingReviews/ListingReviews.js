import styles from "./ListingReviews.module.css";

import { useDispatch, useSelector } from "react-redux";

import { getReviewsByProductId } from "../../../store/reviews";

import ListingReviewsBreakdown from "./ListingReviewsBreakdown/ListingReviewsBreakdown";
import ListingReviewsList from "./ListingReviewsList/ListingReviewsList";
import { useEffect, useRef } from "react";

export default function ListingReviews({ product, setReviewPosition }) {
    const dispatch = useDispatch();
    const ref = useRef();

    if (ref.current) setReviewPosition(ref.current.offsetTop);

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
