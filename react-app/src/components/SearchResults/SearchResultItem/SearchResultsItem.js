import { NavLink } from "react-router-dom";
import styles from "./SearchResultsItem.module.css";
import SearchResultsItemDescription from "./SearchResultsItemDescription/SearchResultsItemDescription";

export default function SearchResultsItem({ product }) {
    return (
        <div className={styles.wrapper}>
            <div className={styles.topHalf}>
                <div className={styles.badge}><span className={styles.amazing}>Amazing's</span> <span className={styles.choice}>Choice</span></div>
                <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                    <img className={styles.image} src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/images/placeholder.png"; }} />
                </NavLink>
            </div>
            <SearchResultsItemDescription product={product} />
        </div>
    );
}
