/*** Arat : ***/

void initPlayer()
{

/*** Üstüne Ekle : ***/

#ifdef UNBLOCK_SYSTEM_ENABLED
PyObject* playerBloktanCikart(PyObject* poSelf, PyObject* poArgs)
{
	CInstanceBase* pMainInstance = CPythonPlayer::Instance().NEW_GetMainActorPtr();
	if (!pMainInstance)
		return Py_BuildValue("i", 0);

	IBackground& rkBG = IBackground::Instance();
	TPixelPosition kPPosTarget, yeniPos;
	pMainInstance->NEW_GetPixelPosition(&kPPosTarget);
	pMainInstance->NEW_GetPixelPosition(&yeniPos);

	if (!rkBG.IsBlock(kPPosTarget.x, kPPosTarget.y))
		return Py_BuildValue("i", 0);

	bool xyBuldu = false;
	for (BYTE i = 0; i < 25 && !xyBuldu; i++)
	{
		if (!rkBG.IsBlock(kPPosTarget.x + i * 100, kPPosTarget.y))
			yeniPos.x += i * 100, xyBuldu = true;

		if (!rkBG.IsBlock(kPPosTarget.x - i * 100, kPPosTarget.y))
			yeniPos.x -= i * 100, xyBuldu = true;

		if (!rkBG.IsBlock(kPPosTarget.x, kPPosTarget.y + i * 100))
			yeniPos.y += i * 100, xyBuldu = true;

		if (!rkBG.IsBlock(kPPosTarget.x, kPPosTarget.y - i * 100))
			yeniPos.y -= i * 100, xyBuldu = true;
	}

	if (!xyBuldu)
	{
		CPythonChat::Instance().AppendChat(CHAT_TYPE_INFO, "Karakteriniz sistem tarafindan kurtarilamadi.");
		return Py_BuildValue("i", 0);
	}

	pMainInstance->NEW_GetPixelPosition(&kPPosTarget);
	float fDstRot = pMainInstance->NEW_GetAdvancingRotationFromPixelPosition(kPPosTarget, yeniPos);
	pMainInstance->SCRIPT_SetPixelPosition(yeniPos.x, yeniPos.y);
	CPythonChat::Instance().AppendChat(CHAT_TYPE_INFO, "Karakteriniz basariyla kurtarildi.");
	return Py_BuildValue("i", 1);
}
#endif

/*** Arat : ***/

		{ "SendDragonSoulRefine",		playerSendDragonSoulRefine,			METH_VARARGS },

/*** Altına müsait bir yere ekle : ***/

#ifdef UNBLOCK_SYSTEM_ENABLED
		{ "BloktanKurtar",				playerBloktanCikart,				METH_VARARGS },
#endif