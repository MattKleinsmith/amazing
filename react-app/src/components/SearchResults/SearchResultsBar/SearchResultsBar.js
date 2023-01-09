import styles from "./SearchResultsBar.module.css";

export default function SearchResultsBar({ products, keywords, showRecent }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                {!showRecent && products.length > 0 && <>
                    {`1-${products.length} of ${products.length} results for`} <span className={styles.keywords}>"{keywords}"</span>
                </>}
                {showRecent && <>
                    <div>Showing <span className={styles.keywords}>most recently</span> added products</div>
                </>}
            </div>
        </div>
    );
}
