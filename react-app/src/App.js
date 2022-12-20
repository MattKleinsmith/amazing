import styles from "./App.module.css";

import { useEffect } from "react";
import { useDispatch } from "react-redux";

import { restoreUser } from "./store/session";

import Header from "./components/Header/Header";
import AppRoutes from "./AppRoutes";
import Footer from "./components/Footer/Footer";
import { setMousePosition } from "./store/ui";

export default function App() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(restoreUser());
  }, [dispatch]);

  const onMouseMove = (e) => {
    // dispatch(updateMousePosition({ x: e.clientX, y: e.clientY }));
  }

  return (
    <>
      <div className={styles.pageContainer} onMouseMove={onMouseMove}>
        <div className={styles.contentWrapper}>
          <Header />
          <AppRoutes />
        </div>
        <Footer />
      </div>
    </>
  );
}
