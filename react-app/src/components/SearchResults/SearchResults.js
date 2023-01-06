import styles from "./SearchResults.module.css";

import { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useSearchParams } from "react-router-dom";

import { getProducts, getProductsByKeywords } from "../../store/products";

import SearchResultsItem from "./SearchResultItem/SearchResultsItem";
// import SearchResultsFilter from "./SearchResultsFilter/SearchResultsFilter";
import SearchResultsBar from "./SearchResultsBar/SearchResultsBar";

export default function SearchResults({ showRecent }) {
    const dispatch = useDispatch();
    const searchParams = useSearchParams()[0];
    const [width, setWidth] = useState(window.innerWidth);

    useEffect(() => {
        if (showRecent) {
            dispatch(getProducts())
        } else {
            dispatch(getProductsByKeywords(searchParams.get("k")))
        }
    }, [dispatch, searchParams, showRecent]);

    useEffect(() => {
        const handleResize = () => setWidth(window.innerWidth);
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, [])

    const products = useSelector(state => Object.values(showRecent ? state.products.all : state.products.filtered));
    if (showRecent) products.reverse();

    let numCols;
    if (width >= 1320) numCols = 4
    else if (width >= 820) numCols = 3
    const products1 = products.slice(0, numCols);
    const products2 = products.slice(numCols);

    return (
        <div className={styles.superWrapper}>
            <SearchResultsBar products={products} keywords={showRecent ? "recent" : searchParams.get("k")} />
            <div className={styles.wrapper}>
                {/* <SearchResultsFilter /> */}
                <div className={styles.results}>
                    <div className={styles.title}>RESULTS</div>
                    <div className={styles.content}>
                        {products1.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={true} product={product} />
                        )}
                    </div>
                    <div className={`${styles.title} ${styles.moreResults}`}>MORE RESULTS</div>
                    <div className={styles.content}>
                        {products2.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={false} product={product} />
                        )}
                    </div>
                </div>
            </div>
        </div >
    );
}
