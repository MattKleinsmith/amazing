import styles from "./SearchResultsItem.module.css";
import SearchResultsItemDescription from "./SearchResultsItemDescription/SearchResultsItemDescription";

export default function SearchResultsItem({ product }) {
    return (
        <div className={styles.wrapper}>
            <img className={styles.image} src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/images/placeholder.png"; }} />
            <SearchResultsItemDescription product={product} />
        </div>
    );
}
