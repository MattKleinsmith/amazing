import styles from "./Homepage.module.css";

import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import SearchResults from "../SearchResults/SearchResults";
import Card from "./Card/Card";
import CardSolo from "./CardSolo/CardSolo";
import { useEffect } from "react";
import { getProductsForHomepage } from "../../store/products";

export default function Homepage() {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const products = useSelector(state => state.products);
    const { phone, makeup, basics } = products.homepage;
    const allProducts = Object.values(products.all);
    const lastProduct = allProducts[allProducts.length - 1];


    useEffect(() => {
        dispatch(getProductsForHomepage());
    }, [dispatch])

    return <div className={styles.wrapper}>
        <img className={styles.banner} src="/images/landing.png" alt="sale" onClick={() => navigate("/s?k=phone")} />
        <div className={styles.cards}>
            <Card products={phone} heading={"Phones"} url="/s?k=phones" />
            <Card products={makeup} heading={"Makeup"} url="/s?k=makeup" />
            <CardSolo product={lastProduct} heading={"Newest product"} url={`/listing/${lastProduct?.id}`} />
            <Card products={basics} heading={"Amazing Basics"} url="/s?k=basics" />
        </div>
        <div className={styles.filler} />
        <SearchResults showRecent={true} isHomepage={true} />
    </div>;
}
