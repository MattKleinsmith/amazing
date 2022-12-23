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

    let products = useSelector(state => Object.values(state.products.filtered));

    const width = document.documentElement.clientWidth * window.devicePixelRatio;
    const numCols = width > 1879 ? 4 : 3;  // Calibrate to media queries
    const products2 = products.slice(numCols);
    products = products.slice(0, numCols);

    return (
        <div className={styles.superWrapper}>
            <div className={styles.wrapper}>
                <div className={styles.filter}></div>
                <div className={styles.results}>
                    <div className={styles.title}>RESULTS</div>
                    <div className={styles.content}>
                        {products.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={true} product={product} />
                        )}
                    </div>
                    <div className={styles.title}>MORE RESULTS</div>
                    <div className={styles.content}>
                        {products2.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={false} product={product} />
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
