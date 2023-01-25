import styles from "./App.module.css";

import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import { restoreUser } from "./store/session";
import { getAddresses } from "./store/addresses";

import Header from "./components/Header/Header";
import AppRoutes from "./AppRoutes";
import Footer from "./components/Footer/Footer";
import Modals from "./components/Modals/Modals";

import { useLocation } from "react-router";

export default function App() {
  const dispatch = useDispatch();
  const location = useLocation();

  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(restoreUser()).then(() => setIsLoaded(true));
    dispatch(getAddresses()).catch(e => { });
  }, [dispatch]);

  if (!isLoaded) return;

  return (
    <>
      <div className={`${styles.pageContainer} ${location.pathname === "/cart" && styles.cartContainer}`}>
        <div className={location.pathname === "/" ? styles.contentWrapperHomepage : styles.contentWrapper}>
          <Header />
          <AppRoutes />
        </div>
        <Footer />
      </div>

      <Modals />
    </>
  );
}
