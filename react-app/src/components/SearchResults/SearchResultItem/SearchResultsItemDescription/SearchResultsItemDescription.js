import styles from "./SearchResultsItemDescription.module.css";
import FiveStars from '../../../FiveStars/FiveStars'

export default function SearchResultsItemDescription({ product }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.title}>{product.title}</div>
            {product.product_rating &&
                <div className={styles.rating}>
                    <FiveStars rating={product.product_rating} isBlack={true} />
                    ({product.num_product_ratings})
                </div>
            }
            <div className={styles.price}><strong>${parseFloat(product.price).toFixed(2)}</strong></div>
        </div>
    );
}
