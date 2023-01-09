import styles from "./Homepage.module.css";

import { useNavigate } from "react-router-dom";
import { useSelector } from "react-redux";

import SearchResults from "../SearchResults/SearchResults";
import Card from "./Card/Card";
import CardSolo from "./CardSolo/CardSolo";

export default function Homepage() {
    const navigate = useNavigate();

    const products = useSelector(state => state.products);
    const { phone, makeup, basics } = products.homepage;
    const allProducts = Object.values(products.all);
    const lastProduct = allProducts[allProducts.length - 1];

    return <div className={styles.wrapper}>
        <img className={styles.banner} src="/images/landing.png" alt="sale" onClick={() => navigate("/s?k=phone")} />
        <div className={styles.cards}>
            <Card products={phone} heading={"Phones"} />
            <Card products={makeup} heading={"Makeup"} />
            <CardSolo product={lastProduct} heading={"Newest product"} />
            <Card products={basics} heading={"Amazing Basics"} />
        </div>
        <div className={styles.filler} />
        <SearchResults showRecent={true} isHomepage={true} />
    </div>;
}
