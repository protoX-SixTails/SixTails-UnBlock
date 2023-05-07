/*** Müsait bir yere ekle ***/

#ifdef UNBLOCK_SYSTEM_ENABLED
	PyModule_AddIntConstant(poModule, "UNBLOCK_SYSTEM_ENABLED", 1);
#else
	PyModule_AddIntConstant(poModule, "UNBLOCK_SYSTEM_ENABLED", 0);
#endif