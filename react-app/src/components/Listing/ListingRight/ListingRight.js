import styles from "./ListingRight.module.css";

import Price from "../../Price/Price";

export default function ListingRight({ product }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.price}>
                    <Price product={product} />
                    <div className={styles.count}>(${product.price} / Count)</div>
                </div>
                <div className={`prime ${styles.prime}`} />
                <div className={styles.freeReturns}>FREE Returns</div>
                <div className={styles.delivery}>FREE delivery <span className={styles.date}>Tuesday, December 27.</span> Order within <span className={styles.deadline}>10 hrs 13 mins</span></div>
                <div className={styles.hr} />
            </div>
        </div>
    );
}
