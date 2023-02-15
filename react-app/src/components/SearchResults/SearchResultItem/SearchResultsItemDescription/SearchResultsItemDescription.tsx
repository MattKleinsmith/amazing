import styles from "./SearchResultsItemDescription.module.css";

import { NavLink } from "react-router-dom"

import Stars from '../../../Stars/Stars'
import Price from "../../../Price/Price";

export default function SearchResultsItemDescription({ product }) {
    const recentDate = new Date();
    recentDate.setDate(recentDate.getDate() + 2);
    const deliveryDate = recentDate.toLocaleDateString('en-us', { weekday: "short", month: "short", day: "numeric" });
    return (
        <div className={styles.wrapper}>
            <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }} className={styles.title}>
                {product.title}
            </NavLink>

            <div className={styles.count}>1 Count (Pack of 1)</div>

            {
                <div className={styles.ratingRow}>
                    <div className={styles.rating}>{product.avg_rating && product.avg_rating.toFixed(1)}</div>
                    <Stars rating={product.avg_rating} />
                    <NavLink to={`/listing/${product.id}`} className={styles.numRatings}>({product.num_ratings})</NavLink>
                </div>
            }

            <div className={styles.priceWrapper}>
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                    <Price product={product} />
                </NavLink>
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }} className={styles.perCount}>
                    (${parseFloat(product.price).toFixed(2)}/Count)
                </NavLink>
            </div>

            <div className={`prime ${styles.prime}`} />

            <div className={styles.delivery}>FREE delivery <span className={styles.date}>{deliveryDate}</span></div>
        </div >
    );
}
