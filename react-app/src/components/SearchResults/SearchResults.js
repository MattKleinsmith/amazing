import styles from "./SearchResults.module.css";

import { useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

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
        <div className={styles.superWrapper}>

            <div className={styles.wrapper}>
                <div className={styles.filter}>Filter</div>
                <div className={styles.content}>
                    {products.map((product, i) =>
                        <SearchResultsItem key={i} product={product} />
                    )}
                </div >
            </div>
        </div>
    );
}
