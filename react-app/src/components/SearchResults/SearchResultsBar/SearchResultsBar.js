import styles from "./SearchResultsBar.module.css";

export default function SearchResultsBar({ products, keywords }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>{products.length > 0 && `1-${products.length} of `} {products.length} results for <span className={styles.keywords}>"{keywords}"</span></div>
        </div>
    );
}
