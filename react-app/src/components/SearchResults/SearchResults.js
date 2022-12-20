import { NavLink, useParams } from "react-router-dom";
import { useSelector } from 'react-redux';

import styles from "./SearchResults.module.css";
import SearchResultsItem from "./SearchResultItem/SearchResultsItem";

export default function SearchResults({ isHomepage = false }) {
    const { categoryName } = useParams();
    let products = useSelector(state => Object.values(state.products));
    if (categoryName) products.reverse();
    if (isHomepage) products = products.slice(products.length - 10);

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                {products.map((product, i) =>
                    <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                        <SearchResultsItem product={product} />
                    </NavLink>)
                }
            </div >
        </div>
    );
}
