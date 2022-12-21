import { NavLink, useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./SearchResults.module.css";
import SearchResultsItem from "./SearchResultItem/SearchResultsItem";
import { useEffect } from "react";
import { getProductsByKeywords } from "../../store/products";

export default function SearchResults() {
    const dispatch = useDispatch();
    const searchParams = useSearchParams()[0];

    useEffect(() => {
        dispatch(getProductsByKeywords(searchParams.get("k")))
    }, [dispatch, searchParams]);

    const products = useSelector(state => Object.values(state.products.filtered));

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
