import styles from "./SearchResults.module.css";

import { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useSearchParams } from "react-router-dom";

import { getProducts, getProductsByKeywords } from "../../store/products";

import SearchResultsItem from "./SearchResultItem/SearchResultsItem";
// import SearchResultsFilter from "./SearchResultsFilter/SearchResultsFilter";
import SearchResultsBar from "./SearchResultsBar/SearchResultsBar";
import { clearReviews } from "../../store/reviews";

export default function SearchResults({ showRecent, isHomepage }) {
    const dispatch = useDispatch();
    const searchParams = useSearchParams()[0];
    const [width, setWidth] = useState(window.innerWidth);
    const [isLoaded, setIsLoaded] = useState(false);

    document.title = showRecent ? "Amazing. Spend less. Smile more." : `Amazing : ${searchParams.get("k")}`;

    useEffect(() => {
        async function fetchData() {
            if (showRecent) {
                await dispatch(getProducts());
            } else {
                await dispatch(getProductsByKeywords(searchParams.get("k")));
            }
            setIsLoaded(true);
        }
        fetchData();
    }, [dispatch, searchParams, showRecent]);

    useEffect(() => {
        dispatch(clearReviews());
        const handleResize = () => setWidth(window.innerWidth);
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, [dispatch])

    let products = useSelector(state => Object.values(showRecent ? state.products.all : state.products.filtered));
    if (showRecent) products = products.reverse().slice(0, 12);

    let numCols;
    if (width >= 1320) numCols = 4
    else if (width >= 820) numCols = 3
    const products1 = products.slice(0, numCols);
    const products2 = products.slice(numCols);

    if (!isLoaded) return;

    return (
        <div className={styles.superWrapper}>
            {!isHomepage && <SearchResultsBar products={products} keywords={showRecent ? "recent" : searchParams.get("k")} showRecent={showRecent} />}
            <div className={styles.wrapper}>
                {/* <SearchResultsFilter /> */}
                {products1.length > 0 && <div className={styles.results}>
                    {!showRecent && <div className={styles.title}>RESULTS</div>}
                    <div className={styles.content}>
                        {products1.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={true} product={product} />
                        )}
                    </div>
                    {!showRecent && products2.length > 0 && <div className={`${styles.title} ${styles.moreResults}`}>MORE RESULTS</div>}
                    {products2.length > 0 && <div className={styles.content}>
                        {products2.map((product, i) =>
                            <SearchResultsItem key={i} i={i} first={false} product={product} />
                        )}
                    </div>}
                </div>}
                {products1.length === 0 &&
                    <div className={styles.emptyResults}>
                        <div>No products found.</div>
                        <NavLink to="/" className={styles.continue}>Continue shopping</NavLink>
                    </div>
                }
            </div>
        </div>
    );
}
