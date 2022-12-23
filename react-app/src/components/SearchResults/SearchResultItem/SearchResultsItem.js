import styles from "./SearchResultsItem.module.css";

import { NavLink } from "react-router-dom";

import SearchResultsItemDescription from "./SearchResultsItemDescription/SearchResultsItemDescription";

export default function SearchResultsItem({ i, product, first }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.topHalf}>
                {first && i === 0 && <div className={styles.badge}><span className={styles.amazing}>Amazing's</span> <span className={styles.choice}>Choice</span></div>}
                {(!first || i !== 0) && <div className={styles.padding} />}
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                    <img className={styles.image} src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/images/placeholder.png"; }} />
                </NavLink>
            </div>
            <SearchResultsItemDescription product={product} />
        </div>
    );
}
