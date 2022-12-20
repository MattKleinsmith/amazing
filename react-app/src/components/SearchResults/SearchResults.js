import { NavLink, useParams, useSearchParams } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./SearchResults.module.css";
import SearchResultsItem from "./SearchResultItem/SearchResultsItem";
import { useEffect } from "react";
import { getProductsByKeywords } from "../../store/products";

export default function SearchResults({ isHomepage = false }) {
    const dispatch = useDispatch();
    const { categoryName } = useParams();
    const [searchParams, setSearchParams] = useSearchParams();

    useEffect(() => {
        dispatch(getProductsByKeywords(searchParams.get("k")))
    }, [dispatch]);

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
