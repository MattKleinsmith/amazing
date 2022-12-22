import styles from "./SearchResultsItemDescription.module.css";

import { NavLink } from "react-router-dom"

import Stars from '../../../Stars/Stars'

export default function SearchResultsItemDescription({ product }) {
    const price = parseFloat(product.price).toFixed(2);
    const [wholePrice, fractionPrice] = price.split(".");
    return (
        <div className={styles.wrapper}>
            <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }} className={styles.title}>
                {product.title}
            </NavLink>

            <div className={styles.count}>1 Count (Pack of 1)</div>

            {product.avg_rating &&
                <div className={styles.ratingRow}>
                    <div className={styles.rating}>{product.avg_rating.toFixed(1)}</div>
                    <Stars rating={product.avg_rating} />
                    <NavLink to={`/listing/${product.id}`} className={styles.numRatings}>({product.num_ratings})</NavLink>
                </div>
            }

            <div className={styles.priceWrapper}>
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }} className={styles.priceRow}>
                    <div className={styles.symbol}>$</div>
                    <div className={styles.whole}>{wholePrice}</div>
                    <div className={styles.fraction}>{fractionPrice}</div>
                </NavLink>
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }} className={styles.perCount}>
                    (${price}/Count)
                </NavLink>
            </div>

            <div className={styles.prime} />

            <div className={styles.delivery}>FREE delivery <span className={styles.date}>Tue, Dec 27</span></div>
        </div >
    );
}
