import styles from "./App.module.css";

import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import { restoreUser } from "./store/session";
import { getAddresses } from "./store/addresses";

import Header from "./components/Header/Header";
import AppRoutes from "./AppRoutes";
import Footer from "./components/Footer/Footer";
import Modals from "./components/Modals/Modals";

export default function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(restoreUser()).then(() => setIsLoaded(true));
    dispatch(getAddresses());
  }, [dispatch]);

  if (!isLoaded) return;

  return (
    <>
      <div className={styles.pageContainer}>
        <div className={styles.contentWrapper}>
          <Header />
          <AppRoutes />
        </div>
        <Footer />
      </div>

      <Modals />
    </>
  );
}
