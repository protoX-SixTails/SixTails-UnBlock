/*** Arat : ***/

void CPythonPlayer::Update()
{
	NEW_RefreshMouseWalkingDirection();

	CPythonPlayerEventHandler& rkPlayerEventHandler=CPythonPlayerEventHandler::GetSingleton();
	rkPlayerEventHandler.FlushVictimList();

/*** Altına Ekle : ***/

#ifdef UNBLOCK_SYSTEM_ENABLED
	CInstanceBase* pInstance = NEW_GetMainActorPtr();
#endif

/*** Altında Bul : ***/

	if (m_isDestPosition)
	{
		CInstanceBase * pInstance = NEW_GetMainActorPtr();

/*** Değiştir : ***/

	if (m_isDestPosition)
	{
#ifndef UNBLOCK_SYSTEM_ENABLED
		CInstanceBase * pInstance = NEW_GetMainActorPtr();
#endif

/*** Arat : ***/

	__Update_AutoAttack();
	__Update_NotifyGuildAreaEvent();

/*** Altına Ekle : ***/

#ifdef UNBLOCK_SYSTEM_ENABLED
	if (pInstance)
	{
		// pInstance değişkeninin geçerli olup olmadığını kontrol ediyoruz.
		TPixelPosition PixelPosition;
		pInstance->NEW_GetPixelPosition(&PixelPosition);

		static IBackground& rkBG = IBackground::Instance(); // IBackground örneği bir kez oluşturuluyor.
		static const std::string warpMapName = CPythonBackground::Instance().GetWarpMapName(); // Metin dizisi de bir kez elde ediliyor.

		if (rkBG.IsBlock(PixelPosition.x, PixelPosition.y) && warpMapName != "metin2_map_duel") {
			PyCallClassMemberFunc(m_ppyGameWindow, "BloktanKurtarici", Py_BuildValue("(i)", 1));
		}
	}
#endif
