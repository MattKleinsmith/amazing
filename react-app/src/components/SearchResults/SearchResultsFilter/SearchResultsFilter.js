import styles from "./SearchResultsFilter.module.css";

export default function SearchResultsFilter({ product }) {
    return (
        <div className={styles.wrapper}>
            <div>Amazing Prime</div>
            <div>Climate Pledge Friendly</div>
            <div>Department</div>
            <div>Customer Reviews</div>
            <div>Brands</div>
            <div>Price</div>
        </div >
    );
}
