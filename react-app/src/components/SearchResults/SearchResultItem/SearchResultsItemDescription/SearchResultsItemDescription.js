import styles from "./SearchResultsItemDescription.module.css";
import FiveStars from '../../../FiveStars/FiveStars'

export default function SearchResultsItemDescription({ product }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.title}>{product.title}</div>
            {product.avg_rating &&
                <div className={styles.rating}>
                    <FiveStars rating={product.avg_rating} isBlack={true} />
                    ({product.num_ratings})
                </div>
            }
            <div className={styles.price}><strong>${parseFloat(product.price).toFixed(2)}</strong></div>
        </div>
    );
}
