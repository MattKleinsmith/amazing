// import Stars from "../../../Stars/Stars";
import styles from "./ListingReviewsList.module.css"

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { getReviewsByProductId } from "../../../../store/reviews";

export default function ListingReviewsList({ product }) {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getReviewsByProductId(product.id));
    }, [dispatch, product.id]);

    const reviews = useSelector(state => Object.values(state.reviews));

    if (reviews.length === 0 || reviews[0].product_id !== product.id) return;

    return (
        <div className={styles.wrapper}>
            {reviews.map((review, i) => <div key={i}>{review.review}</div>)}
        </div>
    );
}
