import styles from "./ListingMiddle.module.css";

import Stars from "../../Stars/Stars";
import Price from "../../Price/Price";

export default function ListingMiddle({ product }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.title}>{product.title}</div>
                <div className={styles.seller}>A product from {product.seller.fullname}</div>
                <div className={styles.rating}>
                    <Stars rating={product.avg_rating} />
                    <div className={styles.numRatings}>{product.num_ratings} rating{product.num_ratings !== 1 && "s"}</div>
                </div>
                <div className={styles.hr} />
                <div className={styles.price}><Price product={product} /></div>
            </div>
        </div>
    );
}
